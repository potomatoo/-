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
              <!-- <div class="text-center py-3">
                <h1>{{editedItem.movie}}</h1>
              </div> -->

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
          <v-card class="review-detail-modal" tile >
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
										label="comment"
										no-resize
                    rows="1"
										v-model="commentContent"
									></v-textarea>
									<v-btn color="primary" justify="center" @click.native="addComment">댓글 작성</v-btn>
								</v-col>
                <hr>
								<v-col cols="12">
                  <v-list 
                    style="max-height: 150px; border:solid black 1px" 
                    class="overflow-y-auto p-2"
                  >
                    <template v-for="comment in this.detailItem.comments">
                      <v-list-item 
                        style="min-height:30px;"
                        :key="comment.id" 
                      >
                        <span class="pr-3">{{comment.content}}</span>
                        <span class="font-italic text--secondary small"> - {{comment.user.username}}</span>
                        <v-btn
                          v-if="comment.user === getMyUserId  || getMyUsername === 'admin' || is_staff"
                          text
                          small
                          @click="deleteComment(comment.id)"
                        >
                          DELETE
                        </v-btn>
                      </v-list-item>
                    </template>
                  </v-list>
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
              <td class="text-xs-center truncate">{{ props.item.movie.title }}</td>
              <td
                class="text-xs-center table-link"
                @click="showDetail(props.item)"
              >{{ props.item.title }}</td>
              <td class="text-xs-center">{{ props.item.user.username }}</td>
              <td class="justify-center">
                <v-btn
                  v-if="props.item.user.username === getMyUsername || getMyUsername === 'admin' || is_staff"
                  icon
                  class="mx-0"
                  @click="editItem(props.item)"
                >
                  <v-icon color="teal">mdi-pencil</v-icon>
                </v-btn>
                <v-btn
                  v-if="props.item.user.username === getMyUsername  || getMyUsername === 'admin' || is_staff"
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
const token = sessionStorage.getItem("jwt");

export default {
  name: "ReviewList",

  data() {
    return {
      username:'',
      is_staff:'',
      updateCnt: 0,
      dialog: false,
      detail_dialog: false,
      search: "",
      select: { movie_id: 0, movie_name: "---" },
      headers: [
        { text: "#", align: "left", value: "id", sortable: true, width: "1"},
        { text: "Movie", align: "left", value: "movie.title", sortable: true },
        { text: "Title", align: "left", value: "title", sortable: false },
        { text: "Username", align: "left", value: "user.username", sortable: false },
        { text: "Actions", value: "movie", align: "left", sortable: false }
      ],
      detailIndex: -1,
      editedItem: {
				title: "",
				username: '',
        content: "",
        movie: "",
				user: "",
        rank: 0,
        comments: []
      },
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
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      console.log(review_id)
      const data = {
        content: this.commentContent,
				user: user_id,
				review: review_id
      };
			axios.post(`${SERVER_URL}/api/v1/review/${review_id}/comment/create/`, data, options)
			.then(res => {
        console.log(res.data)
        this.commentContent = ''
        axios.get(`${SERVER_URL}/api/v1/review/${review_id}/comment`, options)
          .then( res => {
            console.log(res.data)
            this.detailItem.comments = res.data
          })
			})
			.catch(err => {
				console.error(err)
			})
    },
    
    deleteComment(comment_id) {
			const token = sessionStorage.getItem("jwt");
      const review_id = this.reviews[this.detailIndex].id
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
			axios.delete(`${SERVER_URL}/api/v1/comment/${comment_id}/delete/`, options)
			.then(res => {
        console.log(res)
        axios.get(`${SERVER_URL}/api/v1/review/${review_id}/comment/`, options)
          .then( res => {
            console.log(res.data)
            this.detailItem.comments = res.data
          })
			})
			.catch(err => {
				console.error(err)
			})
		},

    showDetail(item) {
      this.detailIndex = this.reviews.indexOf(item);
      this.detailItem = Object.assign({}, item);
      const token = sessionStorage.getItem("jwt");
      const options = {
				headers: {
          Authorization: "jwt " + token
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

    

    editItem(item) {
      this.editedIndex = this.reviews.indexOf(item);
      this.editedItem = Object.assign({}, item);
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };

      axios
        .get(
          `${SERVER_URL}/api/v1/review/${this.reviews[this.editedIndex].id}`,
          options
        )
        .then(res => {
          console.log(res.data.movie);
          this.editedItem = res.data;
        })
        .catch(error => {
          console.log(error.response);
        });

      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.reviews.indexOf(item);
      

      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      if(confirm("Are you sure you want to delete this review?")) {

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
            alert("자신의 글만 삭제할 수 있습니다.");
            console.log(error.response);
          });
      }
    },

    close() {
      this.dialog = false;
      this.detail_dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
      location.reload(true);
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
            `${SERVER_URL}/api/v1/${this.editedItem.movie}/review/${this.editedItem.id}/update/`, 
            this.editedItem,
            options
          )
          .then(res => {
            console.log(res.data)
          })
          .catch(error => {
            console.log(error.response);
          });
      } else {
        const token = sessionStorage.getItem("jwt");
        const user_id = jwtDecode(token).user_id;
        const reviewURL = `${SERVER_URL}/api/v1/${this.select.movie_id}/review/create/`;
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
    },

    getMovies() {
      const token = sessionStorage.getItem("jwt");
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
    },

    getUserinfo() {
      const token = sessionStorage.getItem("jwt");
      const user_id = jwtDecode(token).user_id;
      console.log(user_id)
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(`${SERVER_URL}/api/v1/userList/`, options)
        .then(res => {
          console.log(res.data[user_id - 1])
          this.is_staff = res.data[user_id - 1].is_staff
        })
        .catch(err => {
          console.error(err);
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
    },

    getMyUserId() {
      if(token){
        const user_id = jwtDecode(token).user_id;
        return user_id;
      } else {
        return -1
      }
    }

  },

  created() {
    this.getMovies();
    this.getUserinfo();
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    detail_dialog(val) {
      val || this.close()
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