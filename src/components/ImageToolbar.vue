<template>
  <div>
    <button @click="$emit('generate-mask')">生成掩膜</button>
    <button @click="$emit('auto-segment')">自动切割</button>
  </div>
</template>

<script>
export default {
  name: "ImageToolbar",
};
</script>
