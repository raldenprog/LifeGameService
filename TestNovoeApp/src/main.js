import App from './RootApp/App'
import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'
import configStore from './Store/configStore'
import {sagaMiddleware} from './Store/configStore'
import rootSaga from './Store/RootSaga'



const store = configStore()

sagaMiddleware.run(rootSaga)


render(<Provider store={store}>
          <App/>
       </Provider>, document.getElementById('react')
     )
