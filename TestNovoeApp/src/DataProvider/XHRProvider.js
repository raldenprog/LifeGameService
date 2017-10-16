import {gcf} from '../config'

let instance = null

export default class XHRProvider {
  constructor() {
    if (instance !== null) {
      return instance
    }
  }

  formRequest = (params) =>
  Object.keys(params)
  .map( (el) =>
  `${encodeURIComponent(el)}=${encodeURIComponent(params[el])}` )
   .join('&')

   requestApi = (params) =>
       fetch(
         new Request(`${gcf.apiHttp}${this.formRequest(params)}`,
              {method: 'GET',
               headers: gcf.Headers,
             })
           )
       .then((response) => response.json())
       .then((json) => json)
       .catch((event) => console.log(event))


}
