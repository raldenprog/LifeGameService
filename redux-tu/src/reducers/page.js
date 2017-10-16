import { SET_YEAR } from '../constants/Page'

const initialState = {
  year: 2016,
  photos: [],
  req: 0
}

export default function page(state = initialState, action) {

  switch (action.type) {
    case SET_YEAR:
      return { ...state, year: action.payload, req: action.req }

    default:
      return state;
  }

}
