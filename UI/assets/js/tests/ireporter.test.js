import faker from 'faker';
import puppeteer from "puppeteer";

jest.setTimeout(200000);

const SignupUrl = "https://katherine95.github.io/iReporter/UI/signup.html";
const LoginUrl = "https://katherine95.github.io/iReporter/UI/index.html";
const userAccountUrl = "https://katherine95.github.io/iReporter/UI/user-account.html"

const user = {
  firstname:faker.name.firstName(),
  lastname:faker.name.lastName(),
  othernames:faker.name.lastName(),
  phonenumber:faker.phone.phoneNumber(), 
  email:faker.internet.email(),
  username:faker.name.firstName(),
  password:faker.name.lastName()
};

let page;
let browser;
const width = 1920;
const height = 1000;

beforeAll(async () => {
  browser = await puppeteer.launch({
    headless: true,
    slowMo: 80,
    args: [`--window-size=${width},${height}`]
  });
  page = await browser.newPage();
  await page.setViewport({ width, height });
});
afterAll(() => {
  browser.close();
});

describe("signup", () => {
  test("user can submit a signup request", async () => {
    await page.goto(SignupUrl);
    await page.waitForSelector('#signup');
    await page.click("input[name=firstname]");
    await page.type("input[name=firstname]", user.firstname);
    await page.click("input[name=lastname]");
    await page.type("input[name=lastname]", user.lastname);
    await page.click("input[name=othernames]");
    await page.type("input[name=othernames]", user.othernames);
    await page.click("input[name=phonenumber]");
    await page.type("input[name=phonenumber]", user.phonenumber);
    await page.click("input[name=email]");
    await page.type("input[name=email]", user.email);
    await page.click("input[name=username]");
    await page.type("input[name=username]", user.username);
    await page.click("input[name=password]");
    await page.type("input[name=password]", user.password);
    // await Promise.all([
    //   page.waitForNavigation({ timeout: 60000, waitUntil: 'domcontentloaded' }),
    //   page.click("button[type=submit]")
    // ]);
    await page.click("button[type=submit]");
    // await page.waitForSelector('#login', { visible: true });
    await page.screenshot({path: 'success.png'});
  });
});

describe("login", () => {
  test("user can submit a login request", async () => {
    await page.goto(LoginUrl);
    await page.waitForSelector('#login');
    await page.click("input[name=username]");
    await page.type("input[name=username]", user.username);
    await page.click("input[name=password]");
    await page.type("input[name=password]", user.password);
    await page.click("button[type=submit]");
    // await page.waitForNavigation({ waitUntil: 'domcontentloaded' });
    // await page.waitForSelector('#redflags', { visible: true });
    await page.screenshot({path: 'success1.png'});
  });
});