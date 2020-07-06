<template>
  <footer class="footer">
    <p>{{ msg }}</p>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  props: {
    msg: String
  }
}
</script>

<style lang="scss">
footer {
  height: 50px;
}
p {
  display: block;
}
</style>