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
          v-if="hover || rating !== 0"
          class="d-flex flex-column justify-content-center transition-fast-in-fast-out grey darken-4 v-card--reveal display-1 text-center white--text"
          style="height: 100%; width: 100%;"
        >
          <div>
            <h5 class="font-weight-bold">{{ movie.title }}</h5>
            <p
              v-for="genre in movie.genre"
              :key="genre.id"
              class="white--text card-genre m-0"
            >{{ genre.name }}</p>
          </div>
          <div @click="review_show=true">
            <v-rating
              v-model="rating"
              background-color="white"
              color="yellow accent-4"
              dense
              half-increments
              hover
              size="18"
            ></v-rating>
          </div>
        </div>
      </v-fade-transition>

      <v-dialog v-model="review_show" max-width="600">
        <MovieModalReview
          :rating="rating"
          :movie="movie"
          @reviewUpdateEvent="ratingCheck"
          @closeEvent="closeReview"
        />
      </v-dialog>

      <v-dialog v-model="detail_show" width="600px">
        <template v-slot:activator="{ on }">
          <v-btn icon color="white" v-on="on">
            <v-icon>mdi-chevron-down</v-icon>
          </v-btn>
        </template>
        <MovieModalDetail :movie="movie" @closeEvent="closeDetail" />
      </v-dialog>
    </v-card>
  </v-hover>
</template>

<script>
import axios from "axios";
import jwtDecode from 'jwt-decode'
import MovieModalDetail from "@/components/MovieModalDetail.vue";
import MovieModalReview from "@/components/MovieModalReview.vue";

export default {
  name: "MovieCard",
  data() {
    return {
      reviews: [],
      rating: 0,
      detail_show: false,
      review_show: false
    };
  },

  components: {
    MovieModalDetail,
    MovieModalReview,
  },

  props: {
    movie: {
      type: Object,
      required: false
    }
  },

  methods: {
    closeDetail() {
      this.detail_show = false;
    },

    closeReview() {
      this.review_show = false;
    },


    // rating한 적이 있는 영화는 별점 표시 (mount되는 시점에서 실행되는 함수)
    ratingCheck() {
      // 현재 영화의 리뷰 목록에서 현재 로그인한 사람의 id를 찾아본다.
      const token = sessionStorage.getItem("jwt");
      const user_id = jwtDecode(token).user_id;
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(
          `http://localhost:8000/api/v1/movie/${this.movie.id}/review/`,
          options
        )
        .then(res => {
          this.reviews = res.data;
          this.reviews.forEach(review => {
            if (review.user === user_id) {
              this.rating = review.rank;
            }
          });
        });
    } // end of ratingCheck()
  },

  mounted() {
    this.ratingCheck();
  },

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