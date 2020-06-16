<template>
  <v-container fluid>
    <v-layout row wrap class="d-flex align-items-center">
      <v-flex xs3 class="d-flex justify-content-end pr-5">
        <v-header>현재 위치</v-header>
      </v-flex>
      <v-flex xs6>
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
        <v-btn
          class="ma-2"
          color="secondary"
          @click="getWeatherMovieList()"
        >날씨기반 추천받기</v-btn>
      </v-flex>
    </v-layout>

    <v-container fluid v-if="weatherMovieList">
      <v-row>
        <v-col v-for="movie in movies" :key="movie.id" :cols="6" sm="3">
          <MovieCard :movie="movie" />
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      select: { state: "서울", code: "11B10101" },
      items: [
        { state: "서울", code: "11B10101" },
        { state: "대전", code: "11C20401" },
        { state: "구미", code: "11H10602" },
        { state: "광주", code: "11F20501" }
      ],
      weatherMovieList: []
		};
	},

	methods: {
		getWeatherMovieList(){
			const API_URL = `/1360000/VilageFcstMsgService/getLandFcst?serviceKey=7r002FWJrOZmqbjLfrDYopN40a1SRIbj9FycuHMeYBjc89qpG%2BMxPpH8HsJGui2edG23nhfPz9OVUWQRqW0QyA%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&regId=${this.select.code}&`
			console.log(API_URL)
			axios.post(API_URL)
				.then(res => {
					console.log(res)
				})
			
			
		}
	},
	watch: {
		loader() {
			const l = this.loader;
			this[l] = !this[l];

			setTimeout(() => (this[l] = false), 3000);

			this.loader = null;
		}
	}
  
};
</script>

<style>
  
</style>