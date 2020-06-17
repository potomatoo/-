<template>
  <v-container fluid>
    <v-layout row  wrap class="d-flex justify-content-between align-items-center">
      <v-flex xs3 class="d-flex justify-content-center">
        <h5 class="m-0">현재 위치</h5>
      </v-flex>
      <v-flex xs3>
        <v-select
          :items="items"
          v-model="select"
          label="Select"
          prepend-icon="mdi-map"
          single-line
          item-text="state"
          item-value="code"
          return-object
        ></v-select>
      </v-flex>
      <v-flex xs3 class="d-flex justify-content-center">
        <v-btn class="m-2" color="secondary" @click="getWeatherMovieList()">추천받기</v-btn>
      </v-flex>
    </v-layout>

    <v-container fluid v-if="show" class="d-flex" style="overflow:auto">
			<v-flex v-for="movie in this.weatherMovieList" :key="movie.id" class="justify-content-center" style="min-width: 200px;">
				<MovieCard class="mx-3" :movie="movie" />
			</v-flex>
    </v-container>

  </v-container>
</template>

<script>
import axios from "axios";
import MovieCard from "@/components/MovieCard.vue";

export default {
	components: {
    MovieCard
  },
  data() {
    return {
      select: { state: "서울", code: "11B10101" },
      items: [
        { state: "서울", code: "11B10101" },
        { state: "대전", code: "11C20401" },
        { state: "구미", code: "11H10602" },
        { state: "광주", code: "11F20501" }
      ],
			weatherMovieList: [],
			show: false
    };
  },

  methods: {
    getWeatherMovieList() {
			this.show = true
      const token = sessionStorage.getItem("jwt");
      const SERVER_URL = "http://localhost:8000";
      const data = {
        location_code: this.select.code
      };
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      console.log(`${SERVER_URL}/api/v1/weather_recommend/`);
      axios
        .post(`${SERVER_URL}/api/v1/weather_recommend/`, data, options)
        .then(res => {
          this.weatherMovieList = res.data
          console.log('이게', this.weatherMovieList)
          console.log(res);
        });
    }
  },
  watch: {

  }
};
</script>

<style>
</style>