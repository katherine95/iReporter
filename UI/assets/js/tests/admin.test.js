/* eslint-disable no-undef */
import puppeteer from 'puppeteer';

const loginUrl = 'https://katherine95.github.io/iReporter/UI/index.html';

const adminUser = {
  firstname: 'cate',
  lastname: 'chep',
  othernames: 'kimetto',
  phonenumber: '0725277948',
  email: 'root@gmail.com',
  username: 'catechep',
  password: 'Cate@95#',
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

describe('admin user login', () => {
  test('an admin user can submit a login request', async () => {
    await page.goto(loginUrl);
    await page.waitForSelector('#login');
    await page.click('input[name=username]');
    await page.type('input[name=username]', adminUser.username);
    await page.click('input[name=password]');
    await page.type('input[name=password]', adminUser.password);
    await page.click('button[type=submit]');
    await page.waitForNavigation({ waitUntil: 'domcontentloaded' });
    await page.waitForSelector('#redflags', { visible: true });
    await page.screenshot({ path: 'success5.png' });
  }, 20000);
});
