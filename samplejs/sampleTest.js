var assert = chai.assert;

describe("日付入力テスト", function() {
  var correctDay = dateCal("2018-04-01", "2018-04-04");
  it("開始日＜終了日", function() {
    assert(correctDay == 4);
  });

  var incorrectDay = dateCal("2018-04-04", "2018-04-01");
  it("開始日＞終了日", function() {
    assert(incorrectDay == -2);
  });

  var sameDay = dateCal("2018-04-01", "2018-04-01");
  it("開始日＝終了日", function() {
    assert(sameDay == 1);
  });

  var endDay_blank = dateCal("2018-04-01", "");
  it("終了日が空", function() {
    assert(endDay_blank == 1);
  });

  var startDay_blank = dateCal("", "2018-04-01");
  it("開始日が空", function() {
    assert(startDay_blank == 1);
  });
});
