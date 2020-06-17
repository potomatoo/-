<template>
  <v-container fluid>
    <v-layout v-if="!finishFlag" row class="d-flex align-items-center">
      <v-flex class="d-flex flex-column align-items-center justify-content-around">
        <h5 class="m-0 pb-3">나만의 배우를 선택해 주세요</h5>
        <v-btn v-if="!left" color="secondary" class="small" @click="next">{{buttonName}}</v-btn>
      </v-flex>
    </v-layout>

    <v-layout v-if="!finishFlag" row class="d-flex justify-content-center">
      <v-flex>
        <v-row>
          <v-col cols="6">
            <WorldcupChoice id="left" :actor="left" @choiceEvent="leftChoice" />
          </v-col>
          <v-col cols="6">
            <WorldcupChoice id="right" :actor="right" @choiceEvent="rightChoice" />
          </v-col>
        </v-row>
      </v-flex>
    </v-layout>

    <v-layout row wrap class="d-flex justify-content-center text-center">
      <div v-if="finishFlag">
        <h3>배우 '{{favorite_actor.name}}'이(가) 출연한 영화들입니다.</h3>
      </div>

      <v-container fluid class="d-flex justify-content-center" style="overflow:auto">
        <v-flex
          v-for="movie in this.favoriteActorMovieList"
          :key="movie.id"
          class="justify-content-center"
          style="min-width: 200px; max-width: 200px"
        >
            <MovieCard class="mx-3" :movie="movie" />
        </v-flex>
      </v-container>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import WorldcupChoice from "@/components/WorldcupChoice.vue";
import MovieCard from "@/components/MovieCard.vue";
export default {
  data() {
    return {
      favoriteActorMovieList: [],
      favorite_actor: "",
      current_round: [],
      next_round: [],
      roundNum: 32,
      left: null,
      right: null,
      finishFlag: false
    };
  },
  components: {
    WorldcupChoice,
    MovieCard
  },

  methods: {
    randomActorCall() {
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get("http://localhost:8000/api/v1/worldcup_recommend/", options)
        .then(res => {
          console.log(res.data);
          // console.log(this.current_round)
          res.data.actors.forEach(code => {
            axios
              .get(`http://localhost:8000/api/v1/actor/${code}/`, options)
              .then(res => {
                // console.log(res.data)
                this.current_round.push(res.data);
              });
          });
        });
    },
    leftChoice() {
      this.next_round.push(this.left);
      this.left = null;
      this.right = null;
      this.next();
    },
    rightChoice() {
      this.next_round.push(this.right);
      this.left = null;
      this.right = null;
      this.next();
    },
    next() {
      this.left = this.current_round.pop();
      this.right = this.current_round.pop();
    }
  },
  computed: {
    buttonName() {
      return this.left === null
        ? "이상형 월드컵 시작하기"
        : `${this.current_round.length}강 시작하기`;
    }
  },
  watch: {
    //라운드 종료 판별
    left: function() {
      if (this.current_round.length === 0 && !this.left) {
        this.current_round = this.next_round;
        this.next_round = [];
        this.roundNum = this.current_round.length;
      }
    },
    //우승자 판별
    right: function() {
      if (
        this.next_round.length === 0 &&
        this.current_round.length === 1 &&
        !this.left &&
        !this.right
      ) {
        this.left = this.current_round.pop();
        console.log(this.left);
        this.favorite_actor = this.left;
        this.finishFlag = true;
      }
    },

    finishFlag: function() {
      const token = sessionStorage.getItem("jwt");
      const SERVER_URL = "http://localhost:8000";
      const data = {
        actor: this.favorite_actor.id
      };
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .post(`${SERVER_URL}/api/v1/actor_recommend/`, data, options)
        .then(res => {
          this.favoriteActorMovieList = res.data;
          console.log(res);
        });
    }
  },
  created() {
    this.randomActorCall();
  }
};
</script>

<style>
</style>