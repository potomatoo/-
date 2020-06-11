import router from "../../router";
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

const state = {
    token: null,
    username: null,
    errors: [],
};

const getters = {
  isLoggedIn: state => !!state.token, // token값이 있는지 확인
  getErrors: state => state.errors,
};

const mutations = {  // setter 개념, 매개변수를 받을 수 있다, 순차적 로직, commit('함수명', '전달인자')로 실행가능
    setToken: (state, token) => {
        state.token = token
        sessionStorage.setItem('jwt', token)
    },
    setUsername: (state, name) => {
        state.username = name
        sessionStorage.setItem('username', name)
    },
    pushError: (state, error) => state.errors.push(error),
    clearErrors: state => state.errors = [],
};

const actions = { // 비동기 처리 로직, mutation을 실행시키는 역할, dispatch('함수명', '전달인자')로 실행 가능
    // state 값을 변경하기 위해서는 commit 메소드를 호출해야한다.
    initialLogin: ({ commit }) => {
        
        const token = sessionStorage.getItem('jwt')
        if (token) {
            commit('setToken', token)
        }
    },

    logout: ({ commit }) => {  // 모든 세션 데이터들을 지우고 login 화면으로 redirect
        commit('setToken', null)
        sessionStorage.removeItem('username')
        sessionStorage.removeItem('my_movies')
        sessionStorage.removeItem('my_reviews')
        router.push('/login')
    },

    
    login: ({ commit, getters }, userData) => {
        commit('clearErrors')
        // 로그인 세션이 남아있다면, 메인 화면으로 리아이렉트
        if (getters.isLoggedIn) {
            router.push('/')
        }
        else {
            //로그인 세션이 남아있지 않다면,
            // axios 요청을 보내고, 받아온 token값과 login 정보를 session에 저장 후, 메인화면으로 redirect
            axios.post(SERVER_URL + '/rest-auth/', userData) 
            .then(token => {
                commit('setToken', token.data.token)
                commit('setUsername', userData.username)
                router.push('/')
            })
            .catch( err => {
                commit('pushError', err.response.status)
            })
        }
    },
    
    pushError: ({ commit }, error) => commit('pushError', error),

    validation: ({ commit, dispatch }, userData) => {
        if (!userData.username) {
            commit('pushError', 'username은 필수항목입니다!')
        }
        if (userData.password.length < 8 ) {
            commit('pushError', 'password가 너무 짧습니다!')
        }
        else {
            dispatch('login', userData)
        }
    },

    signup: ( {commit, getters, dispatch }, {username, email, password1, password2}) => {
        commit('clearErrors')
        if (getters.isLoggedIn) {
            router.push('/')
        }
        else {
            console.log(username)
            if (!username) {
                commit('pushError', 'ID를 입력하세요')
            }
            if (!email) {
                commit('pushError', 'E-mail을 입력하세요')
            }
            if (password1.length < 8 ) {
                commit('pushError', '비밀번호는 8자 이상이어야합니다')
            }
            else {
                if (password1 === password2) {
                    axios.post(SERVER_URL + 'api/v1/user/', {username, email, password1})
                        .then(message => {
                            message
                            const userData = {
                                username, 
                                password1
                            }
                            dispatch('login', userData)
                        })
                        .catch(err => {
                            commit('pushError', err.response.status)
                        })
                }
                else {
                    commit('pushError', '비밀번호가 일치하지 않습니다')
                }
            }

        }
    }

};

export default {
    state,
    getters,
    mutations,
    actions
}