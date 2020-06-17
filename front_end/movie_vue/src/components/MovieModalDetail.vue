<template>
  <v-card tile id="myModal">
    <v-card-title class="pb-0">
      <span class="headline">{{ movie.title }}</span>
    </v-card-title>
    <v-card-title class="py-0">
      <span>({{ movie.title_en }})</span>
    </v-card-title>

    <v-container fluid>
      <v-divider></v-divider>
      <v-row justify="space-around">
        <v-col cols="12">
          <h5>트레일러</h5>
          <div class="embed-responsive embed-responsive-16by9">
            <iframe
							id='myVideo'
              :src="this.iframeSrc"
              frameborder="0"
              class="embed-responsive-item"
            ></iframe>
          </div>
        </v-col>
      </v-row>

      <v-divider></v-divider>
      <v-card-text>
        <div>
          <b>감독</b> |
          <span>{{ movie.director }}</span>
        </div>
        <div>
          <b>배우</b> |
          <span v-for="actor in movie.actors" :key="actor.id">{{ actor.name }}, </span>
        </div>
        <div>
          <b>장르</b> |
          <span v-for="genre in movie.genre" :key="genre.id">{{ genre.name }}, </span>
        </div>
      </v-card-text>

      <v-divider></v-divider>
 
      <v-expansion-panels accordion>
        <v-expansion-panel accordion>
          <v-expansion-panel-header>줄거리</v-expansion-panel-header>
          <v-expansion-panel-content>{{ movie.description }}</v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
			
    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="darken-1" text @click.prevent="closeDetail">닫기</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";
import $ from 'jquery'
const API_KEY = "AIzaSyDq251SEuFTbzlAFosz3mqXb5XiBA94e4o";
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "MovieModalDetail",
  data() {
    return {
      iframeSrc: '',
      tempSrc: ''
    };
  },
  props: {
    movie: {
      type: Object,
      required: false
    }
  },
  methods: {
    closeDetail() {
      this.$emit("closeEvent", true);
      $('iframe#myVideo').attr('src',''); 
      $('iframe#myVideo').attr('src',this.iframeSrc);
    },

    getTrailer() {
      const title = this.movie.title_en;
      console.log(title)
      axios
        .get(API_URL, {
          params: {
            key: API_KEY,
            type: "video",
            part: "snippet",
            maxResults: 1,
            viedeoType: "movie",
            q: `${title} trailer`
          }
        })
        .then(response => {
          this.video = response.data.items[0];
          this.iframeSrc = `http://www.youtube.com/embed/${this.video.id.videoId}`
          this.tempSrc = this.iframeSrc
          console.log(this.iframeSrc)
        })
        .catch(error => {
          console.log(error);
        });
    }
  },

	created() {
    this.getTrailer();
	}
};
 

</script>

<style>
</style>