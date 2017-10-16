import { SET_REQ } from '../constants/Req'

export function setReq(req) {

  return {
    type: SET_REQ,
    payload: req
  }

}
