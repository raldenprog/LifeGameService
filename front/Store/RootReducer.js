import {combineReducers} from	'redux'
import {AuthPageState} from '../AuthPage/ReducersAuthPage'
import {ToolActionsState} from '../ToolActions/ReducerToolActions'
import {TableToolState} from '../ToolTable/ReducerToolTable'

const rootReducer = combineReducers({
  authPageState: AuthPageState,
  toolActions: ToolActionsState,
  // TableToolState,
})

export default rootReducer
