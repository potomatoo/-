<template>

  <div v-if="!!actor" class="d-flex flex-column justify-content-center align-items-center">
    <h3 >{{actor.name}}</h3>
    <div sytle="height:600px;">
        <v-hover
        v-slot:default="{ hover }"
        :open-delay="openDelay"
        :close-delay="closeDelay"
        :disabled="disabled"
        :value="value"
        max-height="600px"
        >
        <v-img
            @click="select"
            :src="actor.img_url"
            alt=""
            :elevation="hover ? 12 : 2"
            style="width: 200px; height:auto !important"
        ></v-img>
        </v-hover>
    </div>
  </div>

</template>

<script>
// import axios from 'axios'
export default {
  data () {
    return {
      movieObject: null,
      disabled: false,
      openDelay: '2',
      closeDelay: '2',
      value: false,
    }
  },
  
  props: {
    actor:{
      type: Object,
      required: false,
    }
  },
  methods: {
    select() {
      this.$emit('choiceEvent', true)
    }
  }
}
</script>

<style>
</style>