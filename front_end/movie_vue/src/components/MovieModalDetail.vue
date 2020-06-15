<template>
  <v-card tile>
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
							id='yt-player'
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
          <span v-for="actor in movie.actor" :key="actor">{{ actor.name }}, </span>
        </div>
        <div>
          <b>장르</b> |
          <span v-for="genre in movie.genre" :key="genre">{{ genre.name }}, </span>
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
const API_KEY = "AIzaSyAuJI_t1RcMzDDAl86DCk0L9yQIeaHVq5A";
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "MovieModalDetail",
  data() {
    return {
			iframeSrc: ''
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
			this.iframeSrc = ''
    },

   
    getTrailer() {
      const title = this.movie.title_en;
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
        })
        .catch(error => {
          console.log(error);
        });
    }
  },

	updated() {
    this.getTrailer();
		
	}
};


</script>

<style>
</style>