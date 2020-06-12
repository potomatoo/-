<template>
  <div>
      <v-card
        class="mx-auto"
        max-width="800"
      >
				<v-toolbar color="grey">
					<v-toolbar-title> Movie List </v-toolbar-title>
					<v-spacer></v-spacer>
					<v-btn icon>
						<v-icon>mdi-magnify</v-icon>
					</v-btn>
				</v-toolbar>

				<v-container fluid v-if="movies.length">
					<v-row>
						<v-col
							v-for="movie in movies"
							:key="movie.id"
							xs="12"
							s="6"
							md="3"
						>
							<MovieCard :movie="movie"/>
						</v-col>
					</v-row>	
				</v-container>
				<v-container v-else>
					<h5 class="my-3">영화 목록을 보려면 로그인을 먼저 해주세요!</h5>
					<v-btn
						:loading="loginbtn"
						:disabled="loginbtn"
						color="blue-grey"
						class="ma-2 white--text"
						href="/login"
					>
						Log in
						<v-icon right dark>mdi-account-check</v-icon>
					</v-btn>
				</v-container>
			</v-card>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
		name: "MovieList",
		components: {
			MovieCard,
		},
		props: {
			movies: {
				type: Array,
			}
		}
}
</script>

<style>

</style>