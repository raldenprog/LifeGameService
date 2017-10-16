import	rootReducer	from	'./RootReducer'
import {createStore, applyMiddleware} from 'redux'
import createSagaMiddleware from 'redux-saga'


const logger = (store) => (next) => (action) => {
  console.log('dispatching', action)
  let result = next(action)
  console.log('next state', store.getState())
 return result
}


export const sagaMiddleware = createSagaMiddleware()
export let wsDispatch = null

const configureStore = () => {
		const	store	=	createStore(rootReducer, applyMiddleware(logger, sagaMiddleware))
    wsDispatch = store.dispatch
    return	store
}

export default configureStore
