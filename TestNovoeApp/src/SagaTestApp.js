import {put, takeLatest} from 'redux-saga/effects'
import XHRProvider from './DataProvider/XHRProvider.js'
import * as types from './ActionTypesTestApp.js'
import {gcf} from './config'

const xhr = new XHRProvider()


function* fectchContent(action) {
  const response = yield xhr.requestApi({
      path: action.path,
      fields: gcf.filedsParam
    })
  if (response) {
    yield put(
      {
        type: types.GET_METADATA,
        metadataFolder: response,
      }
    )
  } else {
    console.log('Failed')
  }
}


export function* AppSaga() {
  yield takeLatest( types.FETCH_METADATA, fectchContent )
}
