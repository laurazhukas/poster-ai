<template>
  <transition name="new-survey">
    <div>My page!</div>
  </transition>
</template>

<script>
export default {

}
</script>

<style>
.new-survey-enter-active {
  transition: all .3s ease;
}
.new-survey-leave-active {
  opacity: 0;
  transition: all .0s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.new-survey-enter, .new-survey-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
