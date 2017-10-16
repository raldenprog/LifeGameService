
import * as types from './ActionTypesTestApp'


export const FETCH_METADATA = (path) => {
  return {type: types.FETCH_METADATA, path}
}

export const GET_METADATA = (metadataFolder) => {
  return { type: types.GET_METADATA, metadataFolder}
}
