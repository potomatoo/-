<template>
  <v-layout row wrap>
    <v-flex xs6>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-flex>

    <v-flex xs12>
      <v-data-table :headers="headers" :items="reviews" :search="search">
        <template slot="items" slot-scope="props">
          <tr>
            <td>{{ props.item.movie }}</td>
            <td class="text-xs-right">{{ props.item.id }}</td>
            <td class="text-xs-right">{{ props.item.movie }}</td>
            <td class="text-xs-right">{{ props.item.title }}</td>
            <td class="text-xs-right">{{ props.item.content }}</td>
          </tr>
        </template>

        <v-alert
          class="mt-3"
          slot="no-results"
          text
          dense
          color="info"
          icon="mdi-magnify"
          border="left"
        >Your search for "{{ search }}" found no results</v-alert>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>



<script>
import { mapGetters } from "vuex";
import axios from "axios";
const SERVER_URL = "http://localhost:8000";

export default {
  name: "ReviewList",

  components: {},

  data() {
    return {
      search: "",

      headers: [
        {
          text: "#",
          align: "left",
          value: "id",
          sortable: true
        },
        {
          text: "Movie",
          align: "left",
          value: "movie",
          sortable: true
        },
        {
          text: "Title",
          align: "left",
          value: "title",
          sortable: false
        },
        {
          text: "Content",
          value: "content",
          sortable: false
        }
      ]
    };
  },

  props: {
    reviews: {
      type: Array
    }
  },

  methods: {
    getMovieName() {
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      this.reviews.forEach((review, index) => {
        axios
          .get(`${SERVER_URL}/api/v1/movie/${review.movie}`, options)
          .then(res => {
            this.reviews[index].movie = res.data.title;
          })
          .catch(error => {
            console.log(error.response);
          });
      });
    }
  },

  computed: {
    ...mapGetters(["isLoggedIn"])
  },

  updated() {
    this.getMovieName();
  }
};
</script>

<style>
</style>