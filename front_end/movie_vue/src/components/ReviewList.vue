<template>
  <div>
    <v-layout row wrap class="justify-space-around align-items-center">
      <v-flex xs6>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Movie title"
          single-line
          hide-details
        ></v-text-field>
      </v-flex>

      <v-flex xs2>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" darkx v-on="on">New Reivew</v-btn>
          </template>

          <v-card class="movie-review-modal" tile>
            <v-card-title>
              <span class="headline">{{formTitle}}</span>
            </v-card-title>

            <v-container fluid>
              <div class="text-center py-3">
                <h1>{{editedItem.movie}}</h1>
              </div>

              <div class="text-center">
                <v-rating
                  v-model="editedItem.rank"
                  background-color="orange-lighten-3"
                  color="orange"
                  dense
                  half-increments
                  hover
                  size="30"
                ></v-rating>
              </div>

              <v-row>
                <v-col cols="12" v-if="editedIndex < 0">
                  <v-select
                    v-model="select"
                    :items="movies"
                    item-text="movie_name"
                    item-value="id"
                    label="영화 선택"
                    persistent-hint
                    return-object
                    single-line
                  ></v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="제목" v-model="editedItem.title"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea label="내용" v-model="editedItem.content"></v-textarea>
                </v-col>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click.native="close">취소하기</v-btn>
                  <v-btn color="blue darken-1" text @click.native="save">작성하기</v-btn>
                </v-card-actions>
              </v-row>
            </v-container>
          </v-card>
        </v-dialog>
      </v-flex>
    </v-layout>

    <v-layout row wrap class="justify-space-around align-items-center">
      <v-flex xs2>
        <v-dialog v-model="detail_dialog" max-width="600px">
          <v-card class="review-detail-modal" tile>
            <v-card-title>
              <span class="headline">리뷰 상세보기</span>
            </v-card-title>

            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-card-title>{{detailItem.title}}</v-card-title>
                  <v-card-subtitle class="pb-0 mt-3">작성일: {{$moment(detailItem.created_at).format("YYYY년 MM월 DD일 hh시 mm분")}}</v-card-subtitle>
                  <v-card-subtitle class="py-0">수정일: {{$moment(detailItem.updated_at).format("YYYY년 MM월 DD일 hh시 mm분")}}</v-card-subtitle>
                </v-col>
                <v-col cols="12">
                  <v-card-text>{{detailItem.content}}</v-card-text>
                </v-col>
                <v-col cols="12">
                  <div>
                    <v-card-text class="d-inline">평점:</v-card-text>
                    <v-rating
                      class="d-inline"
                      v-model="detailItem.rank"
                      background-color="orange-lighten-3"
                      color="orange"
                      dense
                      readonly
                      half-increments
                      size="20"
                    ></v-rating>
                  </div>
                </v-col>

								<v-col cols="12">
									<hr>
									<v-textarea
										label="Text"
										filled
										auto-grow
										v-model="commentContent"
									></v-textarea>
									<v-btn color="primary" @click.native="addComment">댓글 작성</v-btn>
								</v-col>

								<v-col cols="12">
									<ul>
										<li v-for="comment in this.detailItem.comments" :key="comment.id"> {{comment.content}}</li>
									</ul>
								</v-col>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click.native="close">닫기</v-btn>
                </v-card-actions>
              </v-row>
            </v-container>
          </v-card>
        </v-dialog>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs12>
        <v-data-table :headers="headers" :items="reviews" :search="search">
          <template slot="item" slot-scope="props">
            <tr>
              <td class="text-xs-center" style="width: 15px">{{ props.item.id }}</td>
              <td class="text-xs-center truncate">{{ props.item.movie }}</td>
              <td
                class="text-xs-center table-link"
                @click="showDetail(props.item)"
              >{{ props.item.title }}</td>
              <td class="text-xs-center">{{ props.item.user }}</td>
              <td class="justify-center">
                <v-btn
                  v-if="props.item.user === getMyUsername"
                  icon
                  class="mx-0"
                  @click="editItem(props.item)"
                >
                  <v-icon color="teal">mdi-pencil</v-icon>
                </v-btn>
                <v-btn
                  v-if="props.item.user === getMyUsername"
                  icon
                  class="mx-0"
                  @click="deleteItem(props.item)"
                >
                  <v-icon color="pink">mdi-delete</v-icon>
                </v-btn>
              </td>
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
  </div>
</template>



<script>
import { mapGetters } from "vuex";
import axios from "axios";
import jwtDecode from "jwt-decode";
const SERVER_URL = "http://localhost:8000";

export default {
  name: "ReviewList",

  data() {
    return {
      updateCnt: 0,
      dialog: false,
      detail_dialog: false,
      search: "",
      select: { movie_id: 0, movie_name: "dsfd" },
      headers: [
        { text: "#", align: "left", value: "id", sortable: true },
        { text: "Movie", align: "left", value: "movie", sortable: true },
        { text: "Title", align: "left", value: "title", sortable: false },
        { text: "Username", align: "left", value: "user", sortable: false },
        { text: "Actions", value: "title", align: "left", sortable: false }
      ],
      detailIndex: -1,
      detailItem: {
				title: "",
				username: '',
				created_at: '',
				updated_at: '',
        content: "",
        movie: "",
				user: "",
				commments: [],
        rank: 0
      },
      editedIndex: -1,
      editedItem: {
        title: "",
        content: "",
        movie: "",
        user: "",
        rank: 0
      },
      defaultItem: {
        title: "",
        content: "",
        movie: "",
        user: "",
        rank: 0
      },
			movies: [],
			commentContent: '',
    };
  },

  props: {
    reviews: {
      type: Array
    }
  },

  methods: {
		addComment() {
			const token = sessionStorage.getItem("jwt");
      const user_id = jwtDecode(token).user_id;
      const review_id = this.reviews[this.detailIndex].id
      const SERVER_URL = "http://localhost:8000/api/v1";
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      // const data = {
      //   content: this.commentContent,
			// 	// user: user_id,
			// 	// review: review_id
      // };
      // console.log(data);
      console.log(review_id)
      const data = {
        content: this.commentContent,
				user: user_id,
				review: review_id
      };
			axios.post(`${SERVER_URL}/review/${review_id}/comment/create/`, data, options)
			.then(res => {
        console.log(res.data)
			})
			.catch(err => {
				console.error(err)
			})
		},

    showDetail(item) {
      this.detailIndex = this.reviews.indexOf(item);
      this.detailItem = Object.assign({}, item);
      const token = sessionStorage.getItem("jwt");
			// const review_id = this.reviews[this.detailIndex].id
      const options = {
				headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(`${SERVER_URL}/api/v1/review/`,options)
        .then(res => {
					console.log(res.data)
        })
        .catch(error => {
          console.log(error.response);
        });

      this.detail_dialog = true;
    },

    changeIdToName() {
      if (this.updateCnt === 0) {
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
              this.review.title_name = res.data.title;
            })
            .catch(error => {
              console.log(error.response);
            });
        });

        this.reviews.forEach((review, index) => {
          axios
            .get(`${SERVER_URL}/api/v1/user/${review.user}`, options)
            .then(res => {
              this.reviews[index].user = res.data.username;
            })
            .catch(error => {
              console.log(error.response);
            });
        });
        this.updateCnt++;
      }
    },

    editItem(item) {
      this.editedIndex = this.reviews.indexOf(item);
      this.editedItem = Object.assign({}, item);
      const token = sessionStorage.getItem("jwt");
      const user_id = jwtDecode(token).user_id;
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      this.editedItem.user = user_id;

      axios
        .get(
          `${SERVER_URL}/api/v1/review/${this.reviews[this.editedIndex].id}`,
          options
        )
        .then(res => {
          console.log(res.data.movie);
          this.editedItem.movie = res.data.movie;
        })
        .catch(error => {
          console.log(error.response);
        });

      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.reviews.indexOf(item);
      confirm("Are you sure you want to delete this review?") &&
        this.reviews.splice(index, 0);

      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .delete(
          `${SERVER_URL}/api/v1/review/${this.reviews[index].id}/delete/`,
          options
        )
        .then(res => {
          console.log(res);
          location.reload(true);
        })
        .catch(error => {
          console.log("error");
          alert("자신의 글만 삭제할 수 있습니다.");
          console.log(error.response);
        });
    },

    close() {
      this.dialog = false;
      this.detail_dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.reviews[this.editedIndex], this.editedItem);
        const token = sessionStorage.getItem("jwt");
        const options = {
          headers: {
            Authorization: "JWT " + token
          }
        };
        axios
          .post(
            `${SERVER_URL}/api/v1/review/${
              this.reviews[this.editedIndex].id
            }/update/`,
            this.editedItem,
            options
          )
          .then(res => {
            console.log(res);
          })
          .catch(error => {
            console.log(error.response);
          });
      } else {
        const token = sessionStorage.getItem("jwt");
        const user_id = jwtDecode(token).user_id;
        const reviewURL = "http://localhost:8000/api/v1/review/create/";
        const options = {
          headers: {
            Authorization: "JWT " + token
          }
        };
        const data = {
          title: this.editedItem.title,
          content: this.editedItem.content,
          rank: this.editedItem.rank,
          movie: this.select.movie_id,
          user: user_id
        };
        axios
          .post(reviewURL, data, options)
          .then(res => {
            console.log(res);
          })
          .catch(err => {
            console.error(err);
          });
      }
      this.close();
      location.reload(true);
    },

    getMovies() {
      const token = sessionStorage.getItem("jwt");
      const SERVER_URL = "http://localhost:8000";
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios.get(`${SERVER_URL}/api/v1/movie/`, options).then(res => {
        const temp_movies = res.data;
        temp_movies.forEach(movie => {
          this.movies.push({ movie_id: movie.id, movie_name: movie.title });
        });
      });
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn"]),

    formTitle() {
      return this.editedIndex === -1 ? "새로운 리뷰 작성" : "리뷰 수정하기";
		},

    getMyUsername() {
      const username = sessionStorage.getItem("username");
      return username;
    }
  },
  created() {
    this.getMovies();
  },
  updated() {
    this.changeIdToName();
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  }
};
</script> 

<style>
.truncate {
  max-width: 1px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.table-link {
  color: #0645ad;
  font-weight: bold;
  cursor: pointer;
}

.table-link:hover {
  text-decoration: underline;
}
</style>