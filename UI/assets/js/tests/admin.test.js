import puppeteer from 'puppeteer';

jest.setTimeout(200000);

const loginUrl = 'https://katherine95.github.io/iReporter/UI/index.html';
const adminUserAccountUrl = 'https://katherine95.github.io/iReporter/UI/admin.html';

const admin_User = {
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
    args: [`--window-size=${width},${height}`]
});
page = await browser.newPage();
await page.setViewport({ width, height });
});
// afterAll(() => {
//     browser.close();
// });
  
describe('admin user login', () => {
    test('an admin user can submit a login request', async () => {
        await page.goto(loginUrl);
        await page.waitForSelector('#login');
        await page.click('input[name=username]');
        await page.type('input[name=username]', admin_User.username);
        await page.click('input[name=password]');
        await page.type('input[name=password]', admin_User.password);
        await page.click('button[type=submit]');
        await page.waitForNavigation({ waitUntil: 'domcontentloaded' });
        await page.waitForSelector('#redflags', { visible: true });
        await page.screenshot({ path: 'success5.png' });
    });
});