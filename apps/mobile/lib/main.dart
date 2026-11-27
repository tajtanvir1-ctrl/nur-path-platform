import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

void main() => runApp(const NurPathApp());

/// Native package smoke shell. Product features and persistent preferences are
/// intentionally not implemented here; they require their own task evidence.
class NurPathApp extends StatelessWidget {
  const NurPathApp({super.key, this.locale});

  final Locale? locale;
  static const supportedLocales = [
    Locale('bn'), Locale('en'), Locale('ar'), Locale('ur'),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nur Path',
      locale: locale,
      supportedLocales: supportedLocales,
      localizationsDelegates: GlobalMaterialLocalizations.delegates,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF123D32)),
        scaffoldBackgroundColor: const Color(0xFFF7F5ED),
      ),
      darkTheme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF123D32), brightness: Brightness.dark,
        ),
      ),
      home: const _FoundationShell(),
    );
  }
}

class _FoundationShell extends StatefulWidget {
  const _FoundationShell();

  @override
  State<_FoundationShell> createState() => _FoundationShellState();
}

class _FoundationShellState extends State<_FoundationShell> {
  int _selected = 0;

  static const _ids = ['home', 'quran', 'worship', 'nur-ai', 'more'];
  static const _icons = [
    Icons.home_outlined, Icons.menu_book_outlined, Icons.nightlight_outlined,
    Icons.auto_awesome_outlined, Icons.grid_view_outlined,
  ];
  static const _labels = <String, List<String>>{
    'bn': ['হোম', 'কুরআন', 'ইবাদত', 'নূর AI', 'আরও'],
    'en': ['Home', 'Quran', 'Worship', 'Nur AI', 'More'],
    'ar': ['الرئيسية', 'القرآن', 'العبادة', 'نور AI', 'المزيد'],
    'ur': ['ہوم', 'قرآن', 'عبادت', 'نور AI', 'مزید'],
  };
  static const _preview = <String, String>{
    'bn': 'ডেভেলপমেন্ট প্রিভিউ — ফিচার এখনও চালু হয়নি।',
    'en': 'Development preview — features are not enabled yet.',
    'ar': 'معاينة التطوير — الميزات غير مفعلة بعد.',
    'ur': 'ڈیولپمنٹ پیش نظارہ — فیچرز ابھی فعال نہیں ہیں۔',
  };

  @override
  Widget build(BuildContext context) {
    final language = Localizations.localeOf(context).languageCode;
    final labels = _labels[language] ?? _labels['en']!;
    return Scaffold(
      appBar: AppBar(title: Text(language == 'bn' ? 'নূর পথ' : 'Nur Path')),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(_icons[_selected], size: 48),
                const SizedBox(height: 16),
                Text(labels[_selected],
                  key: ValueKey('foundation-tab-${_ids[_selected]}'),
                  style: Theme.of(context).textTheme.headlineMedium,
                  textAlign: TextAlign.center),
                const SizedBox(height: 8),
                Text(_preview[language] ?? _preview['en']!,
                  textAlign: TextAlign.center),
              ],
            ),
          ),
        ),
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selected,
        onDestinationSelected: (index) => setState(() => _selected = index),
        destinations: List.generate(_ids.length, (index) => NavigationDestination(
          icon: Icon(_icons[index]), label: labels[index],
        )),
      ),
    );
  }
}
