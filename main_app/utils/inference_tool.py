import torch
import torch.nn as nn
from torch.nn import functional as F
from PIL import Image
from torchvision import transforms


__all__ = ['vgg19']
model_urls = {
    'vgg19': 'https://download.pytorch.org/models/vgg19-dcbb9e9d.pth',
}

class VGG(nn.Module):
    def __init__(self, features):
        super(VGG, self).__init__()
        self.features = features
        self.reg_layer = nn.Sequential(
            nn.Conv2d(512, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 1, 1)
        )

    def forward(self, x):
        x = self.features(x)
        x = F.upsample_bilinear(x, scale_factor=2)
        x = self.reg_layer(x)
        return torch.abs(x)


def make_layers(cfg, batch_norm=False):
    layers = []
    in_channels = 3
    for v in cfg:
        if v == 'M':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            if batch_norm:
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
    return nn.Sequential(*layers)

cfg = {
    'E': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512]
}

def vgg19():
    """VGG 19-layer model (configuration "E")
        model pre-trained on ImageNet
    """
    model = VGG(make_layers(cfg['E']))
    # model.load_state_dict(model_zoo.load_url(model_urls['vgg19']), strict=False)
    return model


class InferenceTool:
    def __init__(self, model_path='resources/Weights/best_model.pth', device='cpu'):
        self.model = vgg19()
        self.device = torch.device(device)
        self.model.to(self.device)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.trans = transforms.Compose([
                        transforms.ToTensor(),
                        transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
                    ])
 
    def predict(self, img):
        img = Image.fromarray(img).convert("RGB")
        img = self.trans(img)
        inputs = img.to(self.device)
        inputs = torch.unsqueeze(inputs, 0)
        with torch.set_grad_enabled(False):
            outputs = self.model(inputs)
        return torch.sum(outputs).item()

 
if __name__ == "__main__":
    import cv2
    inference_tool = InferenceTool(model_path='resources/Weights/best_model.pth', device='cpu')
    image = cv2.imread('/Users/huyquang/Downloads/15.jpg')
    print(inference_tool.predict(image))
