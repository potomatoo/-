<template>
  <div class="text-center">
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'Home',

  data() {
    return {
      movies: [],
    }
  },

  components: {
    MovieList,
  },

}
</script>
