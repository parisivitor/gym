import React, { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { AxiosResponse } from 'axios';

interface User {
  cpf: string;
  password: string;
}

interface Token {
  accessToken: string;
  tokenType: string;
}

const Login: React.FC = () => {
  const [user, setUser] = useState<User>({ cpf: '', password: '' });
  const [token, setToken] = useState<Token | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUser({ ...user, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
  event.preventDefault();

  const formData = new FormData();
  formData.append('grant_type', 'password');
  formData.append('username', user.cpf);
  formData.append('password', user.password);


  try {
    const api: any = process.env.REACT_APP_BACKEND_URL
    const response: AxiosResponse<any, any> = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/login`, formData)

    if (response.status === 200) {
      console.log(response)
      setToken({
        accessToken: response.data.access_token,
        tokenType: response.data.token_type,
      });
      console.log(token)
      setError(null);
    } else {
      setError(response.data.error);
      setToken(null);
    }
  } catch (error: any) {
    console.log(error)
    setToken(null);
    setError(error.response.data.message);
  }
};

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="text" name="cpf" value={user.cpf} onChange={handleInputChange} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" name="password" value={user.password} onChange={handleInputChange} />
      </label>
      <br />
      {error && <p>error: {error}</p>}
      {token && <p>Token: {token.tokenType}</p>}
      <button type="submit">Submit</button>
    </form>
  );
};

export default Login;
