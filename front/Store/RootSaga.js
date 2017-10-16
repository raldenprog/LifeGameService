import {AuthPageSaga} from '../AuthPage/SagaAuthPage'
import {ToolActionsSaga} from '../ToolActions/SagaToolActions'
import {ToolTableSaga} from '../ToolTable/SagaToolTable'


export default function* rootSaga() {
  yield [
        AuthPageSaga(),
        ToolActionsSaga(),
        // ToolTableSaga(),
  ]
}
