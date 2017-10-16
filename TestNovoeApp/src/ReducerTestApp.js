
import * as types from './ActionTypesTestApp'


const initialState = {
  currentFolder: null
}


export const TestApp = (state = initialState, action) => {
  switch (action.type) {

    case types.GET_METADATA:
      return {
        ...state,
        currentFolder: action.metadataFolder
      }

    default: return state

  }
}
