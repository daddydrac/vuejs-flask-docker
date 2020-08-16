// external
import _ from 'lodash';

export default {
  install: function(Vue, name = '$_') {
    Object.defineProperty(Vue.prototype, name, { value: _ });
  }
}