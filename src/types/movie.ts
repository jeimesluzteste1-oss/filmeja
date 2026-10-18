export type PostType = 'list' | 'react' | 'review' | 'episodio' | 'lancamento';

export interface EpisodeScheduleItem {
  episodeNumber: number;
  title?: string;
  releaseDate: string;
  releaseTime?: string;
  status?: 'exibido' | 'proximo' | 'a_estrear';
}

export interface SeriesInfo {
  seriesTitle: string;
  originalTitle?: string;
  seasonNumber: number;
  episodeNumber?: number;
  nextEpisodeDate?: string;
  nextEpisodeTime?: string;
  platform: string;
  totalEpisodes?: number;
  schedule?: EpisodeScheduleItem[];
  recapPreviousEpisode?: string;
  whatToExpect?: string;
}

export interface ListItem {
  rank: number;
  title: string;
  year: number;
  director: string;
  posterImage: string;
  whereToWatch: string[];
  whyWatch: string;
  score: number;
  highlightTag?: string;
  reviewSlug?: string;
  cast?: string[];
  synopsis?: string;
  highlightPoints?: string[];
}

export interface FeaturedMovie {
  title: string;
  originalTitle?: string;
  year: number;
  director: string;
  cast: string[];
  duration: string;
  ratingTmdb: number;
  ratingFilmeJa: number;
  whereToWatch: string[];
  trailerYoutubeId?: string;
  synopsis: string;
  pros: string[];
  cons: string[];
  verdict: string;
}

export interface FAQItem {
  question: string;
  answer: string;
}

export interface MoviePost {
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  type: PostType;
  genres: string[];
  publishedAt: string;
  updatedAt: string;
  author: {
    name: string;
    role: string;
    avatar?: string;
  };
  coverImage: string;
  posterImage: string;
  readingTime: string;
  seo: {
    metaTitle: string;
    metaDescription: string;
    keywords: string[];
  };
  featuredMovie?: FeaturedMovie;
  seriesInfo?: SeriesInfo;
  listItems?: ListItem[];
  content: string;
  faqs: FAQItem[];
}
