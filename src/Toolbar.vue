<template>
  <div>
    <b-button @click="$emit('generateMask')">生成掩膜</b-button>
    <b-button @click="$emit('autoSegment')">自动切割</b-button>
  </div>
</template>

<script>
import { BButton } from 'bootstrap-vue';

export default {
  components: {
    BButton
  }
};
</script>
