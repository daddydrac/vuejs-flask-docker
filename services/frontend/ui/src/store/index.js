import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        user: {},
        dark:true
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, token, user) {
            state.status = 'success'
            state.token = token
            state.user = user
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
    },
    actions: {
        login({commit}, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({url:  process.env.VUE_APP_API_URL + '/auth/login', data: user, method: 'POST'})
                    .then(resp => {
                        const token = resp.data.access_token
                        const refresh_token = resp.data.refresh_token
                        const user = resp.data.user
                        localStorage.setItem('token', token)
                        localStorage.setItem('refresh_token', refresh_token)
                        axios.defaults.headers.common['Authorization'] = token
                        commit('auth_success', token, user)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        logout({ commit }) {
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('token')
                localStorage.removeItem('refresh_token')
                delete axios.defaults.headers.common['Authorization']
                commit('auth_success', '', '')
                resolve()
            })
        },
    },
  getters : {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
  },
    modules: {}
})
