/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Get User Info by User ID
* Retrieve the information of the user with the matching user ID.
*
* userId Integer Id of an existing user.
* key String Your Api Key To Access This Site (optional)
* returns User
* */
const getUsersUserId = ({ userId, key }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        userId,
        key,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Your GET endpoint
* Get a list of alert that the user owns
*
* userId String 
* returns List
* */
const getUsersUserIdAlerts = ({ userId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        userId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Your GET endpoint
* Get the alert of a specific ticker for a user
*
* userId String 
* ticker String 
* returns List
* */
const getUsersUserIdAlertsTicker = ({ userId, ticker }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        userId,
        ticker,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Your GET endpoint
*
* userId String 
* ticker String 
* alertId String 
* returns Alert
* */
const getUsersUserIdAlertsTickerAlertId = ({ userId, ticker, alertId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        userId,
        ticker,
        alertId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Update User Information
* Update the infromation of an existing user.
*
* userId Integer Id of an existing user.
* inlineObject InlineObject  (optional)
* returns User
* */
const patchUsersUserId = ({ userId, inlineObject }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        userId,
        inlineObject,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Create New User
* Create a new user.
*
* inlineObject1 InlineObject1  (optional)
* returns User
* */
const postUser = ({ inlineObject1 }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        inlineObject1,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Create a new alert for a specific ticker on a specific event
*
* userId String 
* inlineObject2 InlineObject2  (optional)
* no response value expected for this operation
* */
const postUsersUserIdAlert = ({ userId, inlineObject2 }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        userId,
        inlineObject2,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

module.exports = {
  getUsersUserId,
  getUsersUserIdAlerts,
  getUsersUserIdAlertsTicker,
  getUsersUserIdAlertsTickerAlertId,
  patchUsersUserId,
  postUser,
  postUsersUserIdAlert,
};
