import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:nur_path/main.dart';

void main() {
  testWidgets('foundation shows five destinations and navigates', (tester) async {
    await tester.pumpWidget(const NurPathApp(locale: Locale('en')));
    await tester.pumpAndSettle();
    expect(find.byType(NavigationDestination), findsNWidgets(5));
    expect(find.byKey(const ValueKey('foundation-tab-home')), findsOneWidget);
    await tester.tap(find.text('Quran'));
    await tester.pumpAndSettle();
    expect(find.byKey(const ValueKey('foundation-tab-quran')), findsOneWidget);
  });

  testWidgets('Arabic shell resolves right-to-left direction', (tester) async {
    await tester.pumpWidget(const NurPathApp(locale: Locale('ar')));
    await tester.pumpAndSettle();
    final home = tester.element(find.byKey(const ValueKey('foundation-tab-home')));
    expect(Directionality.of(home), TextDirection.rtl);
  });
}
