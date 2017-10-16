import XHRProvider from './XHRProvider'

let instance = null


export default class ConfigProvider {

  constructor(){
    if( instance !== null ) {return instance}
    this.data = { lang: {
      RU: {
        App: {
          label: 'werty'}
        }
      }
    }
  }

   localyze = (locale = 'RU', component = null) => {
     if(component === null){ throw new Error('bad component') }
     return this.data[locale][component]
   }



}
