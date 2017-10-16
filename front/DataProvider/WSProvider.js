import {wsDispatch} from '../Store/configStore'
/*import {config} from './ConfigProvider.js'*/

let instance = null

export default class WSProvider {

  constructor() {
    if (instance !== null ) {
      return instance
    }
    this.subscribers = []

    const keepAlive = JSON.stringify({
      p_action: 'keep_alive', serviceName: 'akka_toolShop', params: {},
    })

    let uuid = 'a1916e8b-c28c-42d1-9262-4fcce861bf08'

    if (uuid !== null && uuid !== undefined) {
      this._wss = new WebSocket(`ws://172.18.14.52:9004/wss?token=${uuid}`)
    }
    else {
      return null
    }

    this._wss.onopen = (e) => {
      this._connection_ = setInterval( () => {
        this._wss.send(keepAlive)
      }, 5000)
    }

    this._wss.onmessage = ( wsMsg ) => {
         let msg = null
         try {
           msg = JSON.parse(wsMsg.data)
         }
         catch (e) {
           msg = {msg: {listener: 'common', data: wsMsg.data}}
         }
         if (msg.msg !== undefined) {
           this.exec(msg)
         }
         else {
           console.log('no listener found')
         }
    }
     instance = this;
     return instance;
  }

  linkStore = ( dispatchers ) =>
   Object.keys(dispatchers).forEach( (k) =>
     this.subscribers.push({
       listener: k, action: (_) => {
         wsDispatch( dispatchers[k](_.data) )
       },
     }))

  getSubscribers = () =>
    this.subscribers.map( (s) => s.listener )

  exec = (serverMessage) => {
    const applicant = this.subscribers.filter( (subscriber) => {
      if (subscriber.listener === serverMessage.msg.listener) return subscriber
    })

    if (serverMessage.msg.listener === undefined) {
      console.log(`Exception occured! ${serverMessage.msg}`)
    }

    if (applicant.length !== 0) {
      applicant.map((subscriber) =>
        subscriber.action(serverMessage.msg)
      )
    }
    else {
      console.log('serverMessage ', serverMessage.msg)
      console.log('No listener for: '+serverMessage.msg.listener+ '  found')
      return
    }
  }

  send = (e) => {
    let stringifyed = null;
    try {
      stringifyed = JSON.stringify(e)
    } catch (ex) {
      throw new Error(ex)
    }
    this._wss.send(stringifyed)
  }
}
