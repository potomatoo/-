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
        <v-btn class="ma-2" color="secondary" @click="getWeatherMovieList()">날씨기반 추천받기</v-btn>
      </v-flex>
    </v-layout>

    <v-container fluid v-if="weatherMovieList">
      <v-row>
        <v-card elevation="24" max-width="444" class="mx-auto">
          <v-system-bar lights-out></v-system-bar>
          <v-carousel
            :continuous="false"
            :cycle="cycle"
            :show-arrows="false"
            hide-delimiter-background
            delimiter-icon="mdi-minus"
            height="300"
          >
            <v-carousel-item v-for="(slide, i) in slides" :key="i">
              <v-sheet :color="colors[i]" height="100%" tile>
                <v-row class="fill-height" align="center" justify="center">
                  <div class="display-3">{{ slide }} Slide</div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
          </v-carousel>
          <v-list two-line>
            <v-list-item>
              <v-list-item-avatar>
                <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>John Leider</v-list-item-title>
                <v-list-item-subtitle>Author</v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-switch v-model="cycle" label="Cycle Slides" inset></v-switch>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-card>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from "axios";

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
    getWeatherMovieList() {
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
        .get(`${SERVER_URL}/api/v1/weather_recommend/`, data, options)
        .then(res => {
          console.log(res);
        });
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