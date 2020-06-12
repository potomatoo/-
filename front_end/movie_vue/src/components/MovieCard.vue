<template>
  <v-hover v-slot:default="{ hover }">
    <v-card>
      <v-img
        :aspect-ratio="2/3"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        :src="movie.img_url"
      ></v-img>

      <v-fade-transition>
        <div
          v-if="hover"
          class="d-flex flex-column justify-content-center transition-fast-in-fast-out grey darken-4 v-card--reveal display-1 text-center white--text"
          style="height: 100%; width: 100%;"
        >
          <div>
            <h5 class="font-weight-bold">{{ movie.title }}</h5>
            <p
              v-for="genre in genres"
              :key="genre.id"
              class="white--text card-genre m-0"
            >{{ genre }}</p>
          </div>

          <v-rating
            v-model="rating"
            background-color="white"
            color="yellow accent-4"
            dense
            half-increments
            hover
            size="18"
          ></v-rating>

          <v-btn icon color="white">
            <v-icon>mdi-chevron-down</v-icon>
          </v-btn>
        </div>
      </v-fade-transition>

    </v-card>
  </v-hover>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "MovieCard",
  data() {
    return {
      actors: [],
      genres: []
    };
  },

  props: {
    movie: {
      type: Object,
      required: false
    }
  },

  methods: {
    getActorName() {
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      this.movie.actors.forEach(code => {
        axios
          .get(`${SERVER_URL}/api/v1/actor/${code}`, options)
          .then(res => {
            this.actors.push(res.data.name);
          })
          .catch(error => {
            console.log(error.response);
          });
      });
    },

    getGenreName() {
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      this.movie.genre.forEach(code => {
        axios
          .get(`${SERVER_URL}/api/v1/genre/${code}`, options)
          .then(res => {
            this.genres.push(res.data.name);
          })
          .catch(error => {
            console.log(error.response);
          });
      });
    }
  },

  created() {
    this.getGenreName();
    this.getActorName();
  }
};
</script>

<style>
.v-card--reveal {
  align-items: center;
  bottom: 0%;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
}

.card-genre {
  font-size: 14px;
  line-height: 1.5;
  margin: 0;
}
</style>