<template>
  <div id="app">
    <ImageUploader @image-uploaded="loadModelAndPredict" />
    <Toolbar @generate-mask="generateMask" @auto-segment="autoSegment" />
  </div>
</template>

<script>
import ImageUploader from "./components/ImageUploader.vue";
import Toolbar from "./components/ImageToolbar.vue";
import * as onnx from "onnxjs";

export default {
  name: "App",
  components: {
    ImageUploader,
    Toolbar,
  },
  data() {
    return {
      model: null,
    };
  },
  methods: {
    async loadModelAndPredict(imageData) {
      this.model = await this.loadModel();
      await this.predictImage(imageData);
      // 在这里处理预测结果，例如显示在页面上
    },
    async loadModel() {
      const model = new onnx.InferenceSession({ backendHint: "webgl" });
      await model.loadModel("../public/segmentation.onnx");
      return model;
    },
    async predictImage(
      // eslint-disable-next-line no-unused-vars
      imageData
    ) {
      // 在这里实现图像预处理、预测和后处理的逻辑
      // ...
      // 示例占位符预测结果
      // 在这里处理预测结果，例如显示在页面上
    },
    generateMask() {
      // 使用 ONNX 模型生成掩膜
      // ...
    },
    autoSegment() {
      // 使用 ONNX 模型自动切割图像
      // ...
    },
  },
};
</script>
