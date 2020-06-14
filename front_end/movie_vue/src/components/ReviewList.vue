<template>
  <v-layout row wrap>
    <v-flex xs6>
      <v-text-field
        append-icon="search"
        label="Filter"
        single-line
        hide-details
        @input="filterSearch"
      ></v-text-field>
    </v-flex>

    <v-flex xs10>
      <v-data-table
        :headers="headers"
        :items="reviews"
        :item-key="movie"
        :search="filters"
        :custom-filter="customFilter"
      >
        <template slot="headers" slot-scope="props">
          <tr>
            <th v-for="header in props.headers" :key="header.text">{{ header.text }}</th>
          </tr>
        </template>

        <template slot="items" slot-scope="props">
          <tr>
            <td>{{ props.item.movie }}</td>
          </tr>
        </template>
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
      filters: {
        search: ""
      },

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
    customFilter(items, filters, filter, headers) {
      // Init the filter class.
      const cf = new this.$MultiFilters(items, filters, filter, headers);

      cf.registerFilter("search", function(searchWord, items) {
        if (searchWord.trim() === "") return items;

        return items.filter(item => {
            console.log(item)
          return item.movie.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);
      });

      return cf.runFilters();
    },

    filterSearch(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {
        search: val
      });
    },

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
            console.log(res.data.title);
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