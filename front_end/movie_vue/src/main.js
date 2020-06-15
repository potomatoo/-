import Vue from 'vue'
import App from './App.vue'

import router from './router'
import store from './store'

import VueSession from 'vue-session'
import vuetify from './plugins/vuetify';

import MultiFiltersPlugin from './plugins/MultiFilters' 

import VueMoment from 'vue-moment'

Vue.config.productionTip = false

Vue.use(VueMoment);
Vue.use(VueSession)
Vue.use(MultiFiltersPlugin)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
