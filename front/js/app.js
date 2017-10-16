


function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    xhr = null;
  }
  return xhr;
}
function authorisation(login, pass)
{
var str = {
    Login: login,
    Password: pass
  };
var data = JSON.stringify({Data: str});

var xhr = createCORSRequest('POST', 'http://192.168.1.26:13451/auth');
xhr.setRequestHeader(
    'X-Custom-Header', 'value');
xhr.setRequestHeader(
    'Content-Type', 'application/json; charset=utf-8'); 
xhr.setRequestHeader(
    'Access-Control-Allow-Origin', '*');  
xhr.send(data);

xhr.onload = function() {
  alert( this.responseText );
}

xhr.onerror = function() {
  alert( 'Ошибка ' + this.status );
}
} 






var Add = React.createClass({
  getInitialState: function() { //устанавливаем начальное состояние (state)
    return {
      agreeNotChecked: true,
      loginIsEmpty: true,
      textIsEmpty: true
    };
  },
  componentDidMount: function() {
    ReactDOM.findDOMNode(this.refs.login).focus();
  },
  onBtnClickHandler: function(e) {
    e.preventDefault();
    var login = ReactDOM.findDOMNode(this.refs.login).value;
    var text = ReactDOM.findDOMNode(this.refs.text).value;
    authorisation(login, text)  },
  onAuthorChange: function(e) {
    if (e.target.value.trim().length > 0) {
      this.setState({loginIsEmpty: false})
    } else {
      this.setState({loginIsEmpty: true})
    }
  },
  onTextChange: function(e) {
    if (e.target.value.trim().length > 0) {
      this.setState({textIsEmpty: false})
    } else {
      this.setState({textIsEmpty: true})
    }
  },
  render: function() {
    var agreeNotChecked = this.state.agreeNotChecked,
        loginIsEmpty = this.state.loginIsEmpty,
        textIsEmpty = this.state.textIsEmpty;
    return (
      <form className='add cf'>
        <input
          type='text'
          className='add__author'
          onChange={this.onAuthorChange}
          placeholder='логин'
          ref='login'
        />
        <textarea
          className='add__text'
          onChange={this.onTextChange}
          placeholder='пароль'
          ref='text'
        ></textarea>

        <button
          className='add__btn'
          onClick={this.onBtnClickHandler}
          ref='alert_button'
          disabled={loginIsEmpty || textIsEmpty}
          >
          Войти
        </button>
      </form>
    );
  }
});

var App = React.createClass({
  render: function() {
    return (
      <div className='app'>
        <h3>Авторизация</h3>
        <Add />
      </div>
    );
  }
});

ReactDOM.render((
    <App />
), document.getElementById('root'))
