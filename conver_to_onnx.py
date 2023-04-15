import torch
import torchvision

def main():
    model = torchvision.models.segmentation.deeplabv3_resnet50(pretrained=True)
    model.eval()

    # 设置输入张量的大小，例如：(1, 3, 224, 224)
    dummy_input = torch.randn(1, 3, 224, 224)
    onnx_model_path = "segmentation.onnx"

    # 导出 ONNX 模型
    torch.onnx.export(
        model,
        dummy_input,
        onnx_model_path,
        input_names=["input"],
        output_names=["output"],
        opset_version=11,
    )

if __name__ == "__main__":
    main()
