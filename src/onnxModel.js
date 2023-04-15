import * as cv from 'opencv-js';
import * as onnx from 'onnxruntime-web';

// 在这里替换为你的 ONNX 模型文件的路径
const MODEL_PATH = 'path/to/your/onnx/model.onnx';

// 加载 ONNX 模型
const loadModel = async () => {
  const session = new onnx.InferenceSession({ backendHint: 'webgl' });
  await session.loadModel(MODEL_PATH);
  return session;
};

export { loadModel };
