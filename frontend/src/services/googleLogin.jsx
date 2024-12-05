import axios from 'axios';

/**
 *
 * @param {*} accesstoken This is the accesstoken of the user obtained from Google
 */
const googleLogin = async (accesstoken) => {
  try {
      let res = await axios.post('http://localhost:8000/api/google-login/', {
        access_token: accesstoken,
  });
  return Response.data
  } catch(error) {
    console.error("Google login failed", error.response?.data || error.message)
  }
};

export default googleLogin;