/* eslint-disable no-unused-expressions */
/* eslint-disable no-undef */
import faker from 'faker';
import puppeteer from 'puppeteer';

const signupUrl = 'https://katherine95.github.io/iReporter/UI/signup.html';
const loginUrl = 'https://katherine95.github.io/iReporter/UI/index.html';
const createRecordUrl = 'https://katherine95.github.io/iReporter/UI/create-record.html';


const user = {
  firstname: faker.name.firstName(),
  lastname: faker.name.lastName(),
  othernames: faker.name.lastName(),
  phonenumber: '0725277948',
  email: faker.internet.email(),
  username: faker.name.firstName(),
  password: '12345678',
};

const record = {
  comment: 'lets create afakjtests sttsshj tests hghh ahjhs shjhgjhgjhgjhgge te',
  incidentType: 'Redflag',
  location: '45N',
  image: faker.image.imageUrl(),
};

let page;
let browser;
const width = 1920;
const height = 1000;

beforeAll(async () => {
  browser = await puppeteer.launch({
    // headless: false,
    slowMo: 80,
    args: [`--window-size=${width},${height}`],
  });
  page = await browser.newPage();
  await page.setViewport({ width, height });
});
afterAll(() => {
  browser.close();
});

describe('signup', () => {
  test('user can submit a signup request', async () => {
    await page.goto(signupUrl);
    await page.waitForSelector('#signup');
    await page.click('input[name=firstname]');
    await page.type('input[name=firstname]', user.firstname);
    await page.click('input[name=lastname]');
    await page.type('input[name=lastname]', user.lastname);
    await page.click('input[name=othernames]');
    await page.type('input[name=othernames]', user.othernames);
    await page.click('input[name=phonenumber]');
    await page.type('input[name=phonenumber]', user.phonenumber);
    await page.click('input[name=email]');
    await page.type('input[name=email]', user.email);
    await page.click('input[name=username]');
    await page.type('input[name=username]', user.username);
    await page.click('input[name=password]');
    await page.type('input[name=password]', user.password);
    await page.click('button[type=submit]');
    await page.waitForNavigation({ waitUntil: 'domcontentloaded' }),
    await page.waitForSelector('#login', { visible: true });
    await page.screenshot({ path: 'success.png' });
  }, 200000);
});

describe('login', () => {
  test('user can submit a login request', async () => {
    await page.goto(loginUrl);
    await page.waitForSelector('#login');
    await page.click('input[name=username]');
    await page.type('input[name=username]', user.username);
    await page.click('input[name=password]');
    await page.type('input[name=password]', user.password);
    await page.click('button[type=submit]');
    await page.waitForNavigation({ waitUntil: 'domcontentloaded' });
    await page.waitForSelector('#redflags', { visible: true });
    await page.screenshot({ path: 'success1.png' });
  }, 200000);
});

describe('create record', () => {
  test('user can create a record', async () => {
    await page.goto(createRecordUrl);
    await page.waitForSelector('#createIncident');
    await page.click('textarea[name=comment]');
    await page.type('textarea[name=comment]', record.comment);
    await page.click('input[type=radio]');
    await page.type('input[type=radio]', record.incidentType);
    await page.click('input[name=location]');
    await page.type('input[name=location]', record.location);
    await page.click('button[type=submit]');
    await page.waitForNavigation({ waitUntil: 'domcontentloaded' });
    await page.waitForSelector('#redflags', { visible: true });
    await page.screenshot({ path: 'success3.png' });
  }, 200000);
});
