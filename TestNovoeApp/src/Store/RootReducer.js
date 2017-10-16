import {combineReducers} from	'redux'
import {TestApp} from '../ReducerTestApp'

const rootReducer = combineReducers({
  testApp: TestApp
})


export default rootReducer
