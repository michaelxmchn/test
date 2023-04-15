<template>
  <div>
    <input type="file" @change="handleFileUpload" accept="image/*" />
  </div>
</template>

<script>
export default {
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = (e) => {
        this.$emit("image-uploaded", e.target.result);
      };

      reader.readAsDataURL(file);
    },
  },
};
</script>
